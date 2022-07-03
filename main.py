import sqlite3
import tensorflow as tf
import numpy as np
from kivy.core.window import Window
from kivymd.app import MDApp
# from plyer import accelerometer
import time
# accelerometer.enable()
# A_val = accelerometer.acceleration[:3]
# print(A_val)
#create Databse and connect
db=sqlite3.connect("har.db")

#setting up the curser 
cr=db.cursor()




class MainApp(MDApp):


    def build(self):
        # Load the TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path="tflight_model.tflite")
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Test the model on random input data.
        input_shape = input_details[0]['shape']
        input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
        interpreter.set_tensor(input_details[0]['index'], input_data)


        interpreter.invoke()
        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = interpreter.get_tensor(output_details[0]['index'])
        print(output_data)
        print(output_data[0])
        prediction=output_data[0]
        index = np.where(prediction== np.amax(prediction))
        print(index[0])
        if index[0]==[0]:
            print("sitting")
        elif index[0] == [1]:
                print("walking")
        elif index[0]==[2]:
            print("running")






    #     model = TensorFlowModel()
    #     model.load(os.path.join(os.getcwd(), 'tflight_model.tflite'))
    #     np.random.seed(42)
    #     x = np.array(np.random.random_sample(3,8), np.float32)
    #     y = model.pred(x)
    # #     # result should be

    #     return Label(text=f'{y}')


    # accelerometer.enable()
    # X_val, Y_val, Z_val
# #creat tables
    cr.execute("CREATE TABLE IF NOT EXISTS settings(Name text,Age integer,Wight integer,hight integer,job text,user_id integer )" )
    cr.execute("CREATE TABLE IF NOT EXISTS sensor_data(x_axis float,y_axis float,z_axis float,user_id integer)" )
    cr.execute("CREATE TABLE IF NOT EXISTS motivation_tasks(task text, user_id)" )
    my_list=["Ayma","Mohamed","Ahmed","Soliman","Hend","Noiry"]
    # for key,user in  enumerate(my_list):
    #     cr.execute(f"INSERT INTO settings(user_id,Name) VALUES({key+1},'{user}')")
    cr.execute("INSERT INTO settings(user_id,Name) VALUES(1,'Ayman')")
    cr.execute("INSERT INTO settings(user_id,Name) VALUES(1,'Mohamed')")
    cr.execute("INSERT INTO settings(user_id,Name) VALUES(1,'Ahmed')")
    cr.execute("select Name FROM settings")
    user_name=cr.fetchone()
    print(cr.fetchone())
    print(cr.fetchone())

    
    #saving cahnges
    db.commit()


Window.size = (280, 500)
MainApp().run()