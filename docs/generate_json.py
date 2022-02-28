file_obj = open('./docs/tagstoinclude.txt', 'r')
file_lines = file_obj.readlines()
file_obj.close()
output = ''
for line in file_lines:
    output += '        {\n'
    output += '            "include": "#tag-%s.namelist-fcp.pwx"\n'%line[0:-1]
    output += '        },\n'
outfile = open('./docs/generated_json.txt','w')
outfile.write(output)
outfile.close()