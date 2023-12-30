import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question, Choice

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)

def create_choice(question: Question, choice_text: str, votes: int):
    return Choice(question, choice_text, votes)

class QuestionIndesViewTests(TestCase):
    def test_no_questions(self):
        resonse = self.client.get(reverse("polls:index"))
        self.assertEqual(resonse.status_code, 200)
        self.assertContains(resonse, "No polls were available")
        self.assertQuerySetEqual(resonse.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text= "Past Question.", days = -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],
                                 [question])
        
    def test_future_question(self):
        create_question(question_text = "Future question.", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls were available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text = "Past question.", days = -30)
        create_question(question_text = "Future question.", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],
                                 [question])
    
    def test_two_past_question(self):
        q1 = create_question(question_text = "Past question 1.", days = -30)
        q2 = create_question(question_text = "Past question 2.", days = -5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [q2, q1])

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        fq = create_question(question_text = "Future Question", days = 5)
        url = reverse("polls:detail", args = (fq.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        pq  = create_question(question_text = "Past Question", days = -5)
        url = reverse("polls:detail", args = (pq.id,))
        response = self.client.get(url)
        self.assertContains(response, pq.question_text)
        
class QuestionResultsViewTest(TestCase):
    def test_3_choices(self):
        q1 = create_question(question_text = "Question", days = 0)
        c1 = create_choice(question = q1, choice_text = "Option1", votes = 0)
        c2 = create_choice(question = q1, choice_text = "Option2", votes = 4)
        c3 = create_choice(question = q1, choice_text = "Option3", votes = 2)
        url = reverse("polls:results", args = (q1.id,))
        response = self.client.get(url)
        self.assertTrue(response.status_code, 200)

    def test_2_choices(self):
        q1 = create_question(question_text = "Question", days = 0)
        c1 = create_choice(question = q1, choice_text = "Option1", votes = 0)
        c2 = create_choice(question = q1, choice_text = "Option2", votes = 4)
        url = reverse("polls:results", args = (q1.id,))
        response = self.client.get(url)
        self.assertTrue(response.status_code, 200)
        
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        #Returns false for questions who's pub_date is in the future
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)