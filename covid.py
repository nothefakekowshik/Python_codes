from covid import Covid
obj=Covid()
status=obj.get_status_by_country_name("India")
for i in status:
	print(str(i)+" "+str(status[i]))