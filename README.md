# The wagglepy Package

The __wagglepy__ is used to analyze the traces ((of particle, ray, and _e.t.c._)) in variable (could be position $\vec{r}$, velocity $\vec{v}$ or _e.t.c._) space governed by a given system of ordinary differential equations (ODE system) which might come from some specific domains of physics.

The __wagglepy__ package consists of a collection of template notebooks and some utility functionality for drawing and analyzing the particle traces in the study of plasma physics. __Wagglepy__, however, does not restrict itself in particle-tracing, but would expand its application across ray-tracing, stochastic procedure and so on, all of which share the same essence, that is, the ordinary differential system.

For those ode systems that are easy to solve (at least for sympy's **c**omputer **a**lgebra **s**ystem, CAS), we directly use the symbolic solving capability offered by sympy to deduce the exact analytic solution. While for the difficult ones, sympy (and einsteinpy) helps you to, at least, express the problems in a way that the computers can understand, after which the generic functionality concerning perturbation and numerical solver inside __wagglepy__ would try to approximate the solution. 
