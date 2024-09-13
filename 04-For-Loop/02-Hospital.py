doctors = 7
untreated = 0
treated = 0

days = int(input())

for day in range(1, days + 1):
    if day % 3 == 0:
        if untreated > treated:
            doctors += 1
    patients = int(input())

    if patients > doctors:
        treated += doctors
        untreated += patients - doctors
    else:
        treated += patients
print(f'Treated patients: {treated}.\nUntreated patients: {untreated}.')