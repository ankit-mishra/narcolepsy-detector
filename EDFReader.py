from pyedflib import highlevel
from pyedflib import EdfReader

# read an edf file
signals, signal_headers, header = highlevel.read_edf('CHP040.edf')

print('********************************************************************************************************************************', file=open("output.txt", "a"))
f = EdfReader('CHP040.edf')
#print("\nlibrary version: %s" % pyedflib.version.version)

print("\ngeneral header:\n")

print("file duration: %i seconds" % f.file_duration)
print("startdate: %i-%i-%i" % (f.getStartdatetime().day,f.getStartdatetime().month,f.getStartdatetime().year))
print("starttime: %i:%02i:%02i" % (f.getStartdatetime().hour,f.getStartdatetime().minute,f.getStartdatetime().second))
print("patientcode: %s" % f.getPatientCode())
print("gender: %s" % f.getGender())
print("birthdate: %s" % f.getBirthdate())
print("patient_name: %s" % f.getPatientName())
print("patient_additional: %s" % f.getPatientAdditional())
print("admincode: %s" % f.getAdmincode())
print("technician: %s" % f.getTechnician())
print("equipment: %s" % f.getEquipment())
print("recording_additional: %s" % f.getRecordingAdditional())
print("datarecord duration: %f seconds" % f.getFileDuration())
print("number of datarecords in the file: %i" % f.datarecords_in_file)
print("number of annotations in the file: %i" % f.annotations_in_file)

print('****************************************************************', file=open("output.txt", "a"))

for i in header:
    print(i, file=open("output.txt", "a"))

print('****************************************************************', file=open("output.txt", "a"))

for i in signal_headers:
    print(i, file=open("output.txt", "a"))

print('****************************************************************', file=open("output.txt", "a"))

for i in signals:
    print(i, file=open("output.txt", "a"))

print('****************************************************************', file=open("output.txt", "a"))
