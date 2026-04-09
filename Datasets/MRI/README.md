.dcm = DICOM files, the standard format in hospitals.
# pip install pydicom matplotlib
# Convert DICOM → NIfTI (BEST PRACTICE) by pip install dicom2nifti bcz Read NIfTI (much easier for ML) 
the rest of reading,visulaizing you'll find it in the code read_MRI.py
.mha = MetaImage format used by ITK/VTK, 3D Slicer, ITK‑SNAP... his advanget that in Python you can load it with SimpleITK or ITK and immediately get a NumPy volume with correct spacing, without chasing hundreds of .dcm files:
# pip install SimpleITK matplotlib