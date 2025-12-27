
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from blog.models import Category, Post
from django.utils import timezone

def populate():
    # Create Categories
    tech_cat, _ = Category.objects.get_or_create(name='Technology')
    lifestyle_cat, _ = Category.objects.get_or_create(name='Lifestyle')
    coding_cat, _ = Category.objects.get_or_create(name='Coding')

    print("Categories created.")

    # Create Posts
    posts = [
        {
            'title': 'The Future of AI',
            'content': 'Artificial Intelligence is reshaping the world as we know it. From healthcare to finance, AI algorithms are optimizing processes and creating new opportunities. In this post, we explore the potential impacts of AGI and machine learning in the next decade.',
            'category': tech_cat,
            'img_url': 'https://picsum.photos/seed/ai/800/400'
        },
        {
            'title': 'Mastering Django 5',
            'content': 'Django 5 brings a host of new features including better async support and generated model fields. This guide walks you through setting up a modern Django project and deploying it to the cloud using Render.',
            'category': coding_cat,
            'img_url': 'https://picsum.photos/seed/django/800/400'
        },
        {
            'title': 'Remote Work Best Practices',
            'content': 'Working from home offers flexibility but comes with its own set of challenges. Learn how to stay productive, maintain a work-life balance, and communicate effectively with your distributed team.',
            'category': lifestyle_cat,
            'img_url': 'https://picsum.photos/seed/work/800/400'
        },
        {
            'title': 'The Rise of Quantum Computing',
            'content': 'Quantum computers leverage the principles of quantum mechanics to solve problems deemed impossible for classical computers. What does this mean for cryptography and drug discovery?',
            'category': tech_cat,
            'img_url': 'https://picsum.photos/seed/quantum/800/400'
        },
         {
            'title': '10 Tips for Healthy Living',
            'content': 'A healthy lifestyle is more than just diet and exercise. It involves mental well-being, proper sleep, and stress management. Here are 10 actionable tips to improve your daily life.',
            'category': lifestyle_cat,
            'img_url': 'https://picsum.photos/seed/health/800/400'
        },
        {
            'title': 'Getting Started with Python',
            'content': 'Python is one of the most popular programming languages today. Its simplicity and versatility make it perfect for beginners and experts alike. Learn the basics of variables, loops, and functions.',
            'category': coding_cat,
            'img_url': 'https://picsum.photos/seed/python/800/400'
        },
        {
            'title': 'Sustainable Living Guide',
            'content': 'Small changes in your daily routine can have a big impact on the environment. Discover simple ways to reduce waste, save energy, and live a more sustainable life.',
            'category': lifestyle_cat,
            'img_url': 'https://picsum.photos/seed/eco/800/400'
        },
        {
            'title': 'Cybersecurity Essentials',
            'content': 'In a digital world, security is paramount. Protect yourself from phishing, malware, and data breaches with these essential cybersecurity tips for personal and professional use.',
            'category': tech_cat,
            'img_url': 'https://picsum.photos/seed/security/800/400'
        },
        {
            'title': 'The Art of Minimalist Design',
            'content': 'Minimalism is more than just a design trend; it is a philosophy. Learn how to strip away the unnecessary and focus on what truly matters in your web design projects.',
            'category': coding_cat,
            'img_url': 'https://picsum.photos/seed/design/800/400'
        },
        {
            'title': 'Top Travel Destinations 2026',
            'content': 'Looking for your next adventure? From hidden gems in Europe to tropical paradises in Asia, here are the top travel destinations you must visit in 2026.',
            'category': lifestyle_cat,
            'img_url': 'https://picsum.photos/seed/travel/800/400'
        }
    ]

    # ... existing manual posts ...

    # Generate 50 algorithmic posts for pagination testing
    for i in range(1, 51):
        category = [tech_cat, coding_cat, lifestyle_cat][i % 3] # Rotate categories
        posts.append({
            'title': f'The Future of Tech: Insights Part {i}',
            'content': f'This is a generated post to test pagination feature #{i}. In this article, we delve deep into the nuances of technology and lifestyle trends shaping {2025+i}. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'category': category,
            'img_url': f'https://picsum.photos/seed/post{i}/800/400'
        })

    for p_data in posts:
        post, created = Post.objects.get_or_create(
            title=p_data['title'],
            defaults={
                'content': p_data['content'],
                'category': p_data['category'],
                'img_url': p_data['img_url']
            }
        )
        if created:
            print(f"Post created: {post.title}")
        else:
            print(f"Post already exists: {post.title}")

if __name__ == '__main__':
    print("Populating database...")
    populate()
    print("Done!")
