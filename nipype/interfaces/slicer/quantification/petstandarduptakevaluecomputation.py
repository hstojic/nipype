"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os
from nipype.interfaces.slicer.base import SlicerCommandLine


class PETStandardUptakeValueComputationInputSpec(CommandLineInputSpec):
    csvFile = traits.Either(traits.Bool, File(), hash_files=False, desc="A file holding the output SUV values in comma separated lines, one per label. Optional.", argstr="--csvFile %s")
    OutputLabel = traits.Str(desc="List of labels for which SUV values were computed", argstr="--OutputLabel %s")
    OutputLabelValue = traits.Str(desc="List of label values for which SUV values were computed", argstr="--OutputLabelValue %s")
    SUVMax = traits.Str(desc="SUV max for each label", argstr="--SUVMax %s")
    SUVMean = traits.Str(desc="SUV mean for each label", argstr="--SUVMean %s")
    SUVMin = traits.Str(desc="SUV minimum for each label", argstr="--SUVMin %s")


class PETStandardUptakeValueComputationOutputSpec(TraitedSpec):
    csvFile = File(desc="A file holding the output SUV values in comma separated lines, one per label. Optional.", exists=True)


class PETStandardUptakeValueComputation(SlicerCommandLine):
    """title: PET Standard Uptake Value Computation

category: Quantification

description: Computes the standardized uptake value based on body weight. Takes an input PET image in DICOM and NRRD format (DICOM header must contain Radiopharmaceutical parameters). Produces a CSV file that contains patientID, studyDate, dose, labelID, suvmin, suvmax, suvmean, labelName for each volume of interest. It also displays some of the information as output strings in the GUI, the CSV file is optional in that case. The CSV file is appended to on each execution of the CLI.

version: 0.1.0.$Revision: 8595 $(alpha)

documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/ComputeSUVBodyWeight

contributor: Wendy Plesniak (SPL, BWH), Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)

acknowledgements: This work is funded by the Harvard Catalyst, and the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = PETStandardUptakeValueComputationInputSpec
    output_spec = PETStandardUptakeValueComputationOutputSpec
    _cmd = "/home/raid3/gorgolewski/software/slicer/Slicer --launch PETStandardUptakeValueComputation "
    _outputs_filenames = {'csvFile':'csvFile.csv'}
