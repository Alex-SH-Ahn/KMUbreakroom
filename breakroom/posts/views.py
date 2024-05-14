from django.shortcuts import render, redirect
# from .models import Posts, LOCATIONS
from .models import Post, Image, LOCATIONS
from django.contrib.auth.decorators import login_required

def home(request): # 메인 페이지
    selected_location = request.GET.get('location')
    if selected_location: #선택된 위치가 있으면 해당 위치의 글만 보여줌
        # posts = Posts.objects.filter(location=selected_location)
        posts = Post.objects.filter(location=selected_location)
    else:
        # posts = Posts.objects.all()
        posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts, 'selected_location': selected_location, 'locations': LOCATIONS, 'user': request.user})

def detail(request, post_id): # 글 상세 페이지
    # post = Posts.objects.get(id=post_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'detail.html', {'post': post, 'locations': LOCATIONS, 'user': request.user})

@login_required
def new(request): # 새 글 작성
    if request.user.is_authenticated: # 로그인 되어있으면 새 글 작성 가능
        print('function new called')
        return render(request, 'new.html', {'locations': LOCATIONS, 'user': request.user})
    else: # 로그인 되어 있지 않으면 로그인 페이지로 이동
        return redirect('login')

@login_required
def create(request): # 새 글 저장
    error_message = None
    print('function create called')
    if request.method == "POST":
        # post = Posts()
        print('request was POST')
        try:
            post = Post()
            post.author = request.user
            post.name = request.POST['name'] # 공간이름
            post.location = request.POST['location'] # 위치
            # if 'image' in request.FILES: # 이미지가 있으면 이미지 저장
            #     post.image = request.FILES['image']
            post.available_time = request.POST['availableTime'] # 사용시간
            post.how_to_use = request.POST['how_to_use'] # 사용방법
            post.specification = request.POST['specification'] # 사양
            post.save()
            print('post saved')
            for file in request.FILES.getlist('images'):
                image = Image()
                image.post = post
                image.image = file
                image.save()
                print('image saved')
            return redirect('home')
        except Exception as e:
            error_message = str(e).split('\n')[0]  # Extract the first line of the error message
            print(f'Error: {error_message}')
            return new(request, error_message)