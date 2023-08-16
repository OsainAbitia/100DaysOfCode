from pixela_api import Pixela
from datetime import datetime

USERNAME = "ozz"
TOKEN = ""
GRAPH_ID = "gym"

if __name__ == "__main__":
    pixela = Pixela()
    #pixela.create_user(USERNAME, TOKEN)
    #pixela.create_graph_definition(USERNAME, TOKEN, GRAPH_ID)
    
    # Pixels management
    today_timestamp = datetime.now()
    today_formatted = today_timestamp.strftime("%Y%m%d") 
    #pixela.create_pixel(USERNAME, TOKEN, GRAPH_ID, today_formatted)
    #pixela.put_pixel(USERNAME, TOKEN, GRAPH_ID, today_formatted, "1")
    pixela.delete_pixel(USERNAME, TOKEN, GRAPH_ID, today_formatted)