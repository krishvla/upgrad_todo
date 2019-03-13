from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import datetime 
from datetime import timedelta
from upgrad.models import todo, Category


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")), ignore_result=True)
def test():
	da = datetime.datetime.now()
	da = da + datetime.timedelta(days=1)
	today = da.strftime("%Y-%m-%d")
	tds = todo.objects.filter(status="F", due_date = today)
	print("Iam in above loop")
	if len(tds) >0:
		for td in tds:
			print("Iam in for loop")
			stat = td.status
			tdis = td.t_id
			mail_addr = td.gmail
			send_mail('Todo Remainder','This is to remind You about ' + str(td.title) + ' is scheduled Tomorrow','vitstuffofficial@gmail.com',[mail_addr],fail_silently=False)
			todo.objects.filter(t_id = tdis).update(status='T')
			print('Yes is sended mail to: ', mail_addr)



