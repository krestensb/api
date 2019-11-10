import dropbox

dbx = dropbox.Dropbox('_tKcMaV5WXwAAAAAAAAtTeZ39HeF4Hw6FhRRge86h6o9ZkDdlI4RawRMQwBZZPNy')

#print (dbx.users_get_current_account())

for entry in dbx.files_list_folder('/lst_bilag').entries:
    print(entry.name)

print(dbx.files_get_metadata('/lst_bilag/taletilida.odt').server_modified)

dbx.files_upload("taletilida.odt", '//story.txt')
