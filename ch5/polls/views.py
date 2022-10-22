from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View

from .forms import VoteForm

from .models import Question, Choice


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

class VoteView(View):
    def post(self, request, question_id):
        question = Question.objects.get(id=question_id)
        try:
            select_ch = question.choice_set.get(pk=request.POST['choice'])
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'question_id': question.id,
                'error_message': "You didn't select a choice.",
            })
        else:
            select_ch.votes += 1
            select_ch.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# class VoteFormView(View):
#     form_class = VoteForm
#     template_name = "polls/detail.html"
#
#     def get(self, request, pk):
#         question = get_object_or_404(Question, pk)
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form, 'question': question})
#
#     def post(self, request, pk):
#         question = get_object_or_404(Question, pk)
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             try:
#                 selected_choice = question.choice_set.get(pk=request.POST['choice'])
#             except (KeyError, Choice.DoesNotExist):
#                 return render(request, 'polls/detail.html', {
#                     'question': question,
#                     'error_message': "You didn't select a choice.",
#                     'form': form,
#                 })
#             else:
#                 selected_choice.votes += 1
#                 selected_choice.save()
#                 return HttpResponseRedirect(reverse('polls:results', args=(pk,)))


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))