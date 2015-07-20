import csv
import cx_Oracle

#data
#title = ['Project','"Version"','"DuplicateSRID"','"Submit Date"','"SystemReqID"','"HeadLine"','"Description"','"Totally Effort"','"检查SRID字符数"','"检查Headline字符数"']
design_csv = 'd:\\cqimport\\design_csv.csv'
coding_csv = 'd:\\cqimport\\coding_csv.csv'
sr_csv = 'd:\\cqimport\\sr_csv.csv'
sr_title = [('Project',' "Version"',' "State"',' "DuplicateSRID"',' "Submit Date"',' "SystemReqID"',' "HeadLine"',' "Description"',' "Totally Effort"',' "检查SRID字符数"',' "检查Headline字符数"')]
design_title = [('Project',' "CRType"',' "Artifact Type"',' "SRID"',' "Headline"',' "Description"',
                 ' "Module"',' "Owner"',' "Review Peer"',' "Estimate Efforts"',' "Submitter"',
                 ' "Forced Review"',' "Submit_Date"',' "Finish Date"',' "Expect Finish Date"',' "Severity"',' "Priority"',' "Based Ver"',' "CR Property"',' "Discov Phase"',
                 ' "Detect_Env"',' "State"',' "reopenflag"',' "reopenuat"',' "flaghandled"',' "hassolution"',' "uploadtoenv"',
                 ' "uploadtotest"',' "closeflag"',' "flagcrossproject"',' "ispassed"',' "validateflag"',' "SRID字符数检查"')]
coding_title = ''

design_sql = ''

def generate_csv(data,task_type):
    title, csv_file = task_info(task_type)
    writer = csv.writer(csv_file,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerows(title)
    writer.writerows(data)
    csv_file.close()

#generate_csv(data2,'sr')

def open_file(file_path,auth):
    return open(file_path,auth,newline='')

def task_info(task_type):
    if task_type == 'design':
        return design_title, open_file(design_csv,'w')
    elif task_type == 'coding':
        return coding_title, open_file(coding_csv,'w')
    elif task_type == 'sr':
        return sr_title, open_file(sr_csv,'w')
        
    

    """
sr_sql :
SELECT DISTINCT '-',
                 ' "V3.84"',
                 ' "Confirmed"',
                 ' ""',
                 ' "'||TO_CHAR(SYSDATE,'yyyy-mm-dd')||'"',
                 ' "'||ENV.SR_NO||'"',
                 ' "'||REPLACE(SUBSTR(ENV.SR_HEAD_LINE, 10),' ','')||'"',
                 ' "'||REPLACE(SUBSTR(ENV.SR_HEAD_LINE, 10),' ','')||'"',
                 ' "'||'40',
                 ' "'||LENGTH(REPLACE(SUBSTR(ENV.SR_HEAD_LINE, 10),' ',''))||'"',
                 ' "'||LENGTH(REPLACE(SUBSTR(ENV.SR_HEAD_LINE, 10),' ',''))||'"'
   FROM EBAO_NEXT_VERSION ENV WHERE 1=1 
   AND env.is_done = 0 """

def get_sr():
    conn = cx_Oracle.connect('tpdev/tpdevenvpwd@10.1.101.35/ORA35')
    cursor = conn.cursor()
    cursor.execute("""
SELECT * FROM T_USER
""")
    all_data = cursor.fetchall()
    #print(all_data)
    """for item in all_data:
        print(item)"""
    return all_data

generate_csv(get_sr(),'design')
#print(get_sr())
