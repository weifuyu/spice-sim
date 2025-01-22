# DMC directory: "C:\Program Files\QSPICE\dm\bin\dmc.exe"
# DMC make directory: "C:\Program Files\QSPICE\dm\bin\make.exe"

all: clarke iclarke park ipark

clarke: ../../src/transform.c
	"C:\Program Files\QSPICE\dm\bin\dmc.exe" -mn -WD clarke.cpp kernel32.lib ../../src/transform.c

iclarke: ../../src/transform.c
	"C:\Program Files\QSPICE\dm\bin\dmc.exe" -mn -WD iclarke.cpp kernel32.lib ../../src/transform.c

park: ../../src/transform.c
	"C:\Program Files\QSPICE\dm\bin\dmc.exe" -mn -WD park.cpp kernel32.lib ../../src/transform.c

ipark: ../../src/transform.c
	"C:\Program Files\QSPICE\dm\bin\dmc.exe" -mn -WD ipark.cpp kernel32.lib ../../src/transform.c
