#
#  This file is part of the BayesicFitting package.
#
#  BayesicFitting is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
#
#  BayesicFitting is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  The GPL3 license can be found at <http://www.gnu.org/licenses/>.
#
"""
Provides fitter functions.

Import into BayesicFitting itself all classe that are directly usable.
I.e. leave out the base classes and helper classes.

TBC: How much time does this take. Everything is translated ??

"""

from BayesicFitting.source.AmoebaFitter import AmoebaFitter
from BayesicFitting.source.AnnealingAmoeba import AnnealingAmoeba
from BayesicFitting.source.ArctanModel import ArctanModel
#from BayesicFitting.source.BSplinesModel import BSplinesModel
#from BayesicFitting.source.BaseFitter import BaseFitter
#from BayesicFitting.source.BaseModel import BaseModel
from BayesicFitting.source.BracketModel import BracketModel
from BayesicFitting.source.CauchyErrorDistribution import CauchyErrorDistribution
from BayesicFitting.source.CauchyPrior import CauchyPrior
from BayesicFitting.source.ChebyshevPolynomialModel import ChebyshevPolynomialModel
from BayesicFitting.source.CombiModel import CombiModel
from BayesicFitting.source.ConstantModel import ConstantModel
#from BayesicFitting.source.ConvergenceError import ConvergenceError
from BayesicFitting.source.CrossEngine import CrossEngine
from BayesicFitting.source.CurveFitter import CurveFitter
#from BayesicFitting.source.Engine import Engine
from BayesicFitting.source.ErrorDistribution import ErrorDistribution
from BayesicFitting.source.EtalonDriftModel import EtalonDriftModel
from BayesicFitting.source.EtalonModel import EtalonModel
from BayesicFitting.source.ExpModel import ExpModel
#from BayesicFitting.source.Explorer import Explorer
from BayesicFitting.source.ExponentialPrior import ExponentialPrior
from BayesicFitting.source.Fitter import Fitter
#from BayesicFitting.source.FixedModel import FixedModel
#from BayesicFitting.source.FreeShape2dModel import FreeShape2dModel
#from BayesicFitting.source.FreeShapeModel import FreeShapeModel
#from BayesicFitting.source.FrogEngine import FrogEngine
from BayesicFitting.source.GalileanEngine import GalileanEngine
from BayesicFitting.source.GaussErrorDistribution import GaussErrorDistribution
from BayesicFitting.source.GaussModel import GaussModel
from BayesicFitting.source.GaussPrior import GaussPrior
#from BayesicFitting.source.GenGaussErrorDistribution import GenGaussErrorDistribution
from BayesicFitting.source.GibbsEngine import GibbsEngine
from BayesicFitting.source.HarmonicModel import HarmonicModel
from BayesicFitting.source.HyperParameter import HyperParameter
#from BayesicFitting.source.ImageAssistant import ImageAssistant
#from BayesicFitting.source.IterationPlotter import IterationPlotter
#from BayesicFitting.source.IterativeFitter import IterativeFitter
from BayesicFitting.source.JeffreysPrior import JeffreysPrior
from BayesicFitting.source.Kernel2dModel import Kernel2dModel
from BayesicFitting.source.KernelModel import KernelModel
from BayesicFitting.source.LaplaceErrorDistribution import LaplaceErrorDistribution
from BayesicFitting.source.LaplacePrior import LaplacePrior
from BayesicFitting.source.LevenbergMarquardtFitter import LevenbergMarquardtFitter
#from BayesicFitting.source.LinearModel import LinearModel
from BayesicFitting.source.LogFactorial import LogFactorial
from BayesicFitting.source.LorentzModel import LorentzModel
#from BayesicFitting.source.MaxLikelihoodFitter import MaxLikelihoodFitter
#from BayesicFitting.source.Model import Model
from BayesicFitting.source.MonteCarlo import MonteCarlo
from BayesicFitting.source.NestedSampler import NestedSampler
from BayesicFitting.source.NoiseScale import NoiseScale
#from BayesicFitting.source.NonLinearModel import NonLinearModel
#from BayesicFitting.source.OrderEngine import OrderEngine
from BayesicFitting.source.PadeModel import PadeModel
from BayesicFitting.source.Plotter import Plotter
from BayesicFitting.source.PoissonErrorDistribution import PoissonErrorDistribution
from BayesicFitting.source.PolySineAmpModel import PolySineAmpModel
from BayesicFitting.source.PolySurfaceModel import PolySurfaceModel
#from BayesicFitting.source.PolynomialDynamicModel import PolynomialDynamicModel
from BayesicFitting.source.PolynomialModel import PolynomialModel
from BayesicFitting.source.PowerLawModel import PowerLawModel
from BayesicFitting.source.PowerModel import PowerModel
#from BayesicFitting.source.Prior import Prior
from BayesicFitting.source.ProductModel import ProductModel
from BayesicFitting.source.QRFitter import QRFitter
from BayesicFitting.source.RandomEngine import RandomEngine
from BayesicFitting.source.RobustShell import RobustShell
from BayesicFitting.source.Sample import Sample
from BayesicFitting.source.SampleList import SampleList
#from BayesicFitting.source.ScaledErrorDistribution import ScaledErrorDistribution
## import all fitters inside ScipyFitter
from BayesicFitting.source.ScipyFitter import *
from BayesicFitting.source.SincModel import SincModel
from BayesicFitting.source.SineAmpModel import SineAmpModel
from BayesicFitting.source.SineDriftModel import SineDriftModel
from BayesicFitting.source.SineModel import SineModel
from BayesicFitting.source.SineSplineDriftModel import SineSplineDriftModel
from BayesicFitting.source.SineSplineModel import SineSplineModel
from BayesicFitting.source.SplinesModel import SplinesModel
from BayesicFitting.source.StartEngine import StartEngine
from BayesicFitting.source.StepEngine import StepEngine
from BayesicFitting.source.SurfaceSplinesModel import SurfaceSplinesModel
from BayesicFitting.source.UniformPrior import UniformPrior
from BayesicFitting.source.VoigtModel import VoigtModel

from BayesicFitting.source.Formatter import Formatter
from BayesicFitting.source.Tools import Tools



