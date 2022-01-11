import json
import pika
import django
from sys import path
from os import environ



path.append('/media/navanjane/New Volume/University/forth year/blog_reader/blog_reader/settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_reader.settings')
django.setup()
from reader.models import BlogPost

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='blogs')

def callback(ch, method, properties, body):
    print("Received in blogs...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'blog_created':
        blog = BlogPost.objects.create(blog_title=data['blog_title'], blog_content=data['blog_content'])
        blog.save()
        print("blogcreated")
    # elif properties.content_type == 'quote_updated':
    #     quote = Quote.objects.get(id=data['id'])
    #     quote.title = data['title']
    #     quote.save()
    #     print("quote updated")
    # elif properties.content_type == 'quote_deleted':
    #     quote = Quote.objects.get(id=data)
    #     quote.delete()
    #     print("quote deleted")
channel.basic_consume(queue='blogs', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()