import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(id, username, photo,extracted):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='OCR',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO data
                          (id, username, image, extracted) VALUES (%s,%s,%s,%s)"""

        image = convertToBinaryData(photo)
        

        # Convert data into tuple format
        insert_blob_tuple = (id,username,image,extracted)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image  inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(2,"Bala certificate",r"D:\projects\pytesseract_extractor\static\uploads\screenshot1.jpg","Extracted text will be here!")


