from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Subject,GradeComment,ImageVideo
from django.contrib.auth.decorators import login_required
from curriculum.templatetags import extras

@login_required(login_url='login')
def grades(request):
    template_name = 'curriculum/grades.html'
    context = Grade.objects.all()
    return render(request, template_name, {'context': context})

@login_required(login_url='login')
def grades_subjects(request, grade_id):
    template_name = 'curriculum/grade-subject.html'
    grade= Grade.objects.get(id=grade_id)
    subjects= Subject.objects.filter(grade=grade_id)
    image_video = ImageVideo.objects.filter(grade=grade_id)
    comments = GradeComment.objects.filter(grade=grade, parent=None)
    replies = GradeComment.objects.filter(grade=grade).exclude(parent=None)
    rDict = {}
    for reply in replies:
        if reply.parent.id not in rDict.keys():
            rDict[reply.parent.id] = [reply]
        else:
            rDict[reply.parent.id].append(reply)
    return render(request, template_name, {'context': subjects, 'grade':grade, 'comments': comments, 'replyDict': rDict, 'image_video': image_video})

def gradeComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        gradeid = request.POST.get("gradeid")
        grade = Grade.objects.get(id = gradeid)
        parentSno = request.POST.get("parentSno")
        print('parentSno')
        print(parentSno)
        if parentSno == "":
            comment = GradeComment(comment=comment, user=user, grade=grade)
            comment.save()

        else:
            parent = GradeComment.objects.get(id=parentSno)
            comment = GradeComment(comment=comment, user=user, grade=grade, parent=parent)
            
            comment.save()

    return redirect(f"/curriculum/grade/{grade.id}")

