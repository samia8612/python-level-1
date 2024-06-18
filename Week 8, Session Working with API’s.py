import requests #importing the requests module to make HTTP requests
import json  # importing the json module to handle json data

def get_wikipedia_summary(topic):
  #constructing the url to fetch wikipedia summary based on the given topic
  url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
  #making a GET request to fetch data from the url
  response = requests.get(url)
  #checking if the response status code is 200
  if response.status_code == 200:
     data = response.json()
     
     summary = data["extract"]
     # extracting 
     image_url = data.get("thumbnail", {}).get("source")
     #returning an error message if feching information faild
     return summary, image_url
  else:
    return "failed to fetch information. Please try again later.,", None
    
def save_image_from_url(image_url, filename):
  #making a GET 
  response = requests.get(image_url)
  
  if response.status_code == 200:
    with open(filename,"wb")as f:
      f.write(response.content)
    print(f"Image successfully as {filename}")  
    
  else:
    print("faild to fetch image")
    
    
    
def main():
 print ("welcome to Wikipedia summaries")
 topic = input ("Enter a topic you want to learn more about: ")
 summary, image_url = get_wikipedia_summary(topic)
 print("\n summary:")
 print(summary)
 
 if image_url:
   filename=f"{topic.replace(' ','_')}.jpg"
   save_image_from_url(image_url,filename)
 else:
  print ("\nNo image found")
 
if __name__ =="__main__":
  main()
  