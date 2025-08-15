import pydicom

# Télécharge un petit DICOM d'exemple
!wget -q https://github.com/pydicom/pydicom/raw/master/tests/test_files/CT_small.dcm -O sample.dcm

ds = pydicom.dcmread("sample.dcm")
print("Patient:", ds.PatientName)
print("Image shape:", ds.pixel_array.shape)
