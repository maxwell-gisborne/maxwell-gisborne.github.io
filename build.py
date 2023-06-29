#!/bin/env python

from pathlib import Path
import subprocess
import yaml

root = Path.cwd()


def get_markdown_paths(root: Path):
    'bredth first search, find all markdown files'
    queue = [root]
    while len(queue) > 0:
        dir = queue.pop()
        for file in dir.iterdir():
            if file.suffix == '.md':
                yield file
            elif file.is_dir():
                queue.append(file)


def write_html(md_path: Path, lines):
    html_path = md_path.with_suffix('.html')
    with open(html_path, 'w') as file:
        file.write('\n'.join(lines))


def pass_meta(path: Path, meta_string):
    defult = dict(title=path.stem,
                  include=[])
    meta = yaml.safe_load('\n'.join(meta_string))
    if meta is None:
        meta = dict()
    if not isinstance(meta, dict):
        raise ValueError(f'yaml header must be dict\n at {path}')
    return defult | meta




def read_file(path: Path):
    with open(path, 'r') as file:
        lines = file.read().split('\n')

    dashes = []
    for n, line in enumerate(lines):
        if line.startswith('---'):
            dashes.append(n)

    meta_section = []
    raw_head_section = []

    if len(dashes) == 0:
        real_section = lines
    elif len(dashes) == 1:
        n = dashes[0]
        meta_section = lines[:n]
        real_section = lines[n+1:]
    elif len(dashes) >= 2:
        n = dashes[0]
        m = dashes[1]
        meta_section = lines[:n]
        raw_head_section = lines[n+1:m]
        real_section = lines[m+1:]

    return pass_meta(path, meta_section), raw_head_section, real_section


def html_form_markdown(root: Path, markdown_lines: [str]):
    flags = ['links', 'image', 'smarty', 'html',
             'del', 'autolink', 'tabstop',
             'divquote', 'alphalist', 'footnote', 'fencedcode']
    markdown_process = subprocess.run(['/usr/bin/markdown',
                                       '-b', str(root),
                                       '-f', ','.join(flags),
                                       ],
                                      stdout=subprocess.PIPE,
                                      input='\n'.join(markdown_lines),
                                      encoding='utf-8')
    if markdown_process.returncode != 0:
        raise Exception('Markdown Subprocess Failed')

    return markdown_process.stdout.split('\n')


def get_includes(path: Path, meta: dict):
    include_root = Path('includes')
    if not include_root.exists():
        include_root.mkdir()

    include_lines = []
    valid_includes = list(include_root.iterdir())
    for include in meta['include']:
        include = Path(include)
        if path.joinpath(include).exists():
            include = path.joinpath(include)
        if include_root.joinpath(include).exists():
            include = include_root.joinpath(include)
        elif include not in valid_includes:
            raise ValueError(f'Un-known include ({include}) \n file: {path}')

        with open(include, 'r') as file:
            include_lines.extend(file.read().split('\n'))

    return include_lines


def get_style(path: Path, meta: dict):
    style_root = Path('styles')
    if not style_root.exists():
        style_root.mkdir()

    if 'style' in meta:
        style_path = Path(meta['style']).with_suffix('.css')
        if path.joinpath(style_path).exists():
            style_path = path.joinpath(style_path)
        elif style_root.joinpath(style_path).exists():
            style_path = style_root.joinpath(style_path)
        else:
            raise ValueError(f'Could not file style ({style_path})')
    else:
        style_path = style_root.joinpath('defult.css')

    with open(style_path, 'r') as file:
        content = file.read().split('\n')
    return ['<style>', *content, '</style>']


if __name__ == '__main__':
    for path in get_markdown_paths(root):
        print(path)
        meta, raw_head, markdown = read_file(path)
        includes = get_includes(path, meta)

        head = ['<head>',
                *get_style(path, meta),
                f'<title>{meta["title"]}</title>',
                *raw_head,
                *get_includes(path, meta),
                '</head>']

        markdown = ['#' + meta['title']] + markdown
        body = html_form_markdown(root, markdown)

        html = ['<html>',
                *head,
                '<body>', *body, '</body>',
                '</html>']

        write_html(path, html)
