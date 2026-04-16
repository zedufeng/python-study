
#获取文件名
def get_file_name():
    filename=input('请输入文件名')
    try:
        filename=open(filename)
    except:
        FileExistsError
        print('请输入正确的文件名')
    return filename

filename=get_file_name()

#读取csv文件并加载数据
def read_csv(filename):
    sales_date={}
    for name,sale_amount in filename:
        sales_date=sales_date[name,sale_amount]
    return sales_date

sales_date=read_csv(filename)

#找出销售额最高的销售员
def find_highest_sales(sales_date):
    dict=[]
    dict=[(sale_amount,name) for name,sale_amount in sales_date.item()]
    dict.sort(reverse=True,key=lambda x:x[0])
    highest_salesperson=dict[0][0]
    max_sales=dict[0][1]
    return highest_salesperson,max_sales,dict


def calculate_average_sales(sales_date):
    amount=0
    num=0
    for amount in sales_date.value:
        sum+=amount
        num=num+1
    average_sales=sum/num
    return average_sales


def filter_sales_by_range(sales_date,min_sales,max_sales):
    result=[]
    for name,amount in sales_date:
        if min_sales<=amount<=max_sales:
            result.append((name,amount))
    return result

dict=find_highest_sales(sales_date)[2]

def get_top_salespeople(sale_date,n,dict):
    a=print(dict[0:n])
    return a



highest_salesperson=find_highest_sales(sales_date)[0]
average_sales=calculate_average_sales(sales_date)[0]


def save_report(output_file,sales_data,highest_salesperson,average_sale):
    