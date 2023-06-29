title: Conductivity
style: light-mode
include: [ mathjax ]
---

## The definition of conductivity

Conductivity was first defined as the reciprical to resistivity, which is the intensive version of Resistance,
$$ \sigma = \frac{1}{\rho} = \frac{l}{RA} \qquad \left[\Omega^{-1} m^{-1} \right],$$
for a wire of length $l$ and cross section ariea $A$.

Using Ohm's law $V = IR$, for an infinitesimal wire $l$, with area $A$,
$$ E \cdot l =  A \cdot j  \frac{l}{A\sigma}, $$
were $j$ is the current density along the wire thus
$$ j = E \sigma. $$

Considering that the electric field and the curent density are both vectors, that variy over space and time, conductivity is defined as
$$ \vec j(\vec r, t) = \sigma(\vec r, t) \vec E(\vec r, t).  $$

Note, in a two dimentional setting, such as Graphene, we may consider the 2-dimentional current density, and thus the 2-dimentional conductivity, 
which will have units of $J C^{-1} m^{-1}$, and $\Omega^{-1}$, respectivly.

The directoion of the induced current is not allways parralel to the direction of applied electric field,
for example in the Hall effect, where the precence of a magnetic field diflects the induced current, 
thus the conductivity should be considered as a rank-2 tensor, 
$$ j_i(\vec r, t) = \sigma_{ij}(\vec r, t)  E_j(\vec r, t).  $$


## The Drude Model and Mobility

In the Drude Model of conductivity, 
current arrises from charged particles moveing through a meterial in response to an exsternal fuiled $E$.
However, through interactions with the atomis, and with eachother, they loose their momentum over time.

The scattering force is sufficient to remove all of the average particles momentum in timeperiod 
$\tau$, called the scattering time, if the electric field was switched off, $E=0$.

As force is nothing but the instantainouse change in momentum $F = \dot p$,
we can write the scattering force acting on the average particle interms of the scattering time as,
$$ F_{sct} = \frac{ m\bar v }{\tau}, $$
were $m$ is the mass of the average particle, and $\bar v$ is its velocity.

The force applied to the charge carrier by the fild is simply $ F_{ext} = q E $,
were $q$ is the charge of the charge carriers.

Thus we may write the drift velocity of the average particle as
$$ \bar v = \frac{qE\tau}{m}. $$
This is called the drift velocity.

In this model, the drift velocity is proportional to the exsternal field. 
The ratio of the drift velocity to applied filed is called the mobility $\mu$,
$$ \mu = \frac{\bar v }{E}.$$

## Connection with Density of States

If there the density <em>(per-unit-space)</em> of chage carriers is $n$, each with chage $q$, then the conductivity is
$$ \sigma = q n \mu. $$

If however, as in the case of semi-conductors, there are differnet charge carriers,
with different mobilities, and different charges, then 
we must perform an integral to find the correct conductivity,
$$ \sigma = \int_{\mbox{carrier states}} q \cdot n\cdot \mu. $$

If the mobility and charge of the carriers depends only on the energy, then the conductivity becomes
$$ \sigma = \int q(E) \cdot n(E)\cdot \mu(E)\ dE,  $$
were $n(E)$ is the Density of States, with units of <em>per-unit-space per-unit-energy</em>.


## The Boltzman Equation
The Boltzman Equtation describes the movement of a density of particles over phase space $f(\vec r, \vec k, t)$.
It applies the Luivil equation, which describes the flow of such a density when acting in acordance 
with a Hamiltonian $H$, and adds a additional exsplicit time dependence, due to internal collisions.

The Luivil operator is
$$ L = \frac{\partial H}{\partial p_i} \frac{\partial}{\partial r_i} - \frac{\partial H}{\partial r_i}\frac{\partial}{\partial p_i}, $$
were sumation over repeated indicies is assumed.

If we take the Hamiltonian to describe independent particles 
$$ H = \frac{p\^2}{2m} + V(\vec q), $$
Were the potential $V$ givs rise too an exsternal force $F_i = -\frac{\partial V(\vec q)}{\partial q_i}$, 
the Luivil becomes
$$ L = \frac{p_i}{m} \frac{\partial}{\partial r_i} + F_i \frac{\partial}{\partial p_i}.$$

The Luivil Theorum states that, for a conservative system $L f = 0$, however we will assume that there is an additional 
time dependence produced by collisions which gives ries to a drop in dispersion in phase space.
This gives rise to the Bolzman equation,
$$ (\frac{\partial}{\partial t} +  L) f =  \left(\frac{\partial f}{\partial t}\right)_{\mbox{coll}}.$$

For this equation to be usefull, the collision term on the right hand side, must be specified.

The Bolzman Equation can be used to derive a general conservation law.

### static 
Assumeing the collision term is produced by collisions  
of two bodies, we can describe the collison term as 
$$ \left(\frac{\partial f}{\partial t}\right)_{\mbox{coll}} = \iint d\Omega d^{3}p'\ gI(g,\Omega)\ \left[ f(\vec r, \vec p \right].$$

### BVK approximation
The BVK (Bhatnagar, Gross, and Krook) approximation is a simple formula for the collision term in the bolzman equation
which drives the system towards an assymptotic distribution $f\_\infty$, on a time scail of $\tau$,
$$ \left(\frac{\partial f}{\partial t}\right)_c = \frac{f\_\infty - f}{\tau}.$$

### Bolzman Theory for conductivity
[Some usefull notes.](https://edu.itp.phys.ethz.ch/fs14/sst/slides/transport.pdf)

The Bolzman equation can be applied to describe the movement of charge carriers within a  
conductor.
In such a case we can set the collision term to be a BGK  approximation, using the fermi distribution as the assymptotic distribution.
$$ (\partial_t + L) f = \frac{f\_\infty - f}{\tau}, $$
were
$$ f_\infty(\vec k, \vec r, t) = \frac{1}{e^{\frac{\epsilon(\vec k) - \mu}{k_BT}} + 1},$$
for the dispersion relation $\epsilon = \epsilon(\vec k)$.

If we consider a system that is close to the asymptotic distribution,
$$ f = f_0 + \delta f,$$
then we applie the bolzman equation and find
$$\frac{\partial \delta f}{\partial t} + \frac{p_i}{m} \frac{\partial \delta f}{\partial r_i} + F_i \frac{\partial \delta f}{\partial p_i}  + F_i \frac{\partial f\_\infty}{\partial p_i}= - \frac{\delta f}{\tau}.$$

## Free electron conductivity


Around the dirac point charge carriers are described by,
a massless fermion with reduced $\approx c/300$.

Thus we can apply the drude model

m\mu = p / El

El = 


## TDDFT Method
[Paper sugested By Antoinio](https://dft.uci.edu/pubs/BCG05.pdf)

## The Keldysh formalism

For a time dependent hamiltonian of the form
$$ H(t) = H_0 + H'(t), $$
we have a time evolution operator from time $t1$ to $t2$
$$ U(t_2,t_1) = \mathcal{T}exp\int_{t_1}^{t_2}dt'\ H(t').$$

Adopting an interaction picture 
we write the expectation of an operator $\mathcal{O}$ as
$$ \left< \mathcal{O}(t) \right> = \left< n \middle| S^\dagger(t,0) \mathcal{O_I}(t) S(t,0) \middle|n \right>, $$
were 
$$\mathcal{O_I}(t) = U_0^\dagger(t,0) \mathcal{O}(0) U_0(t,0)$$
is the interaction picture observable,
$$ S(t_2,t_1) = U_0^\dagger(t_2,t_1) U(t_2,t_1) $$
evolves the system forwards under the full hamiltonian,
and then removes the effect of the unpaterbed hamiltonian.

We can add a deviation to infinity
$$ \left< \mathcal{O}(t) \right> = \left< n \middle| S^\dagger(t,\infty) S(t,\infty)\mathcal{O_I}(t) S(t,0) \middle|n \right>. $$

we can introduce the Keldysh contor $c$, and write
$$ \left< \mathcal{O}(t) \right> = \left< n \middle| \mathcal{T}_c \mathcal{O}( c )\ exp \left(-i\int dc'\ H'(c')\ \right) \middle|n \right>. $$


## Abinitio Methods
[Review paper](https://dial.uclouvain.be/pr/boreal/object/boreal%3A253988/datastream/PDF_01/view):
First-principles calculations of charge carrier mobility and conductivity in
bulk semiconductors and two-dimensional materials.


### Problem with DFT
Denisty Functional Theory provieds a method to calculate the density of states for a given system, 
however, DFT electronic structure calculateions do not include phonon interactions, 
and are technicaly only valid for the groud state, and thus dont neccesseraly reproduce finite temperature 
phenomena like scattering time.

DFT will allow us to find the electronic states of a crystal, but will reproduce a mechanism by which they decay.
Thus they have infinate lifetimes and $\tau = \infty$.

