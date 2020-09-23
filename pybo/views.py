from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
# Create your views here.


def index(request):
    """목록들 표시하는 것"""
    question_list=Question.objects.order_by('-create_date')
    context={"question_list":question_list}
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    """세부적인 내용을 추가하는것 """
    question= get_object_or_404(Question,pk=question_id) # 여기서 사용된 pk는 Question의 기본키인 id를 의미한다.
    context={'question':question}
    return render(request,'pybo/question_detail.html',context)


def answer_create(request, question_id): # request를 통해서 폼에서 입력한 답변 데이터를 읽을 수 있다.
    """
    답변등록
    """
    question = get_object_or_404(Question,pk=question_id)
    # 그리고 첫번째 매개변수 request 객체를 통해 폼에서 입력한 답변 데이터를 읽을 수 있다.
    # request.POST.get('content')는 POST로 전송된 폼(form) 데이터 항목 중 content의 값을 의미한다.
    # question.answer_set 은 질문의 답변을 의미한다. Question과 Answer은 foreignkey로 연결 되어 있기 때문에 이처럼 사용 할 수 있다.
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail',question_id=question.id)



