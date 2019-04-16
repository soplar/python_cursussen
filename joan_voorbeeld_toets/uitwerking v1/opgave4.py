software = ["Windows Server 2019", "MS SQL Server 2017", "MS Office 2019", "MS Exchange Server 2019", "Microsoft Sharepoint 2016", "MySQL Server"]
for pakket in software:
    if pakket != software[2]:
        print(f"server: {pakket}")
    else:
        print(f"client: {pakket}")
    
