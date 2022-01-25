from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.http import JsonResponse
from .models import*
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import json

rings = 0
rings = int(rings*100)
level = 1
ball_power = 5
wind = 8
elevation = 10
club_used = "Big Topper"

bag = ["Big Topper", "The Big Dawg", "The Goliath", "The Thorn", "The Endbringer", "The Junglist", "The Malibu"]
club_level = [2,5,5,3,1,3,4] #Repeat ???
#bag = ["The Apocalypse", "The Sniper", "The Goliath", "The Thorn", "The Endbringer", "Nirvana", "Houdini"]
#club_level = [6,10,9,9,6,9,9]

balls = [0,3,5,7,10,13]

def get_ring_size(club, level, dist):
	ring_size = ((club[0]["acc_intercept"] + (club[0]["acc_coefficient"]*club[0]["club_accuracy"][level]))*dist)/10
	return (ring_size)

def distance_from_max(club, rings, level, ball_power):
	dist = club[0]["club_distance"][level]*(1+(ball_power/100))
	for r in range(rings):
		r-=1
		dist -= get_ring_size(club, level, dist)/100
	return (dist)

def distance_from_min(club, rings, level, ball_power):
	dist = club[0]["club_min"]*(1+(ball_power/100))
	for r in range(rings):
		r-=1
		dist += get_ring_size(club, level, dist)/100
	return (dist)

def rings_to_adjust(club, level, dist, wind, elevation):
	RingsToAdjust = wind*(1+elevation/100)*((dist**2)/club[0]["traj_coefficient"])/(((club[0]["acc_intercept"] + (club[0]["acc_coefficient"]*club[0]["club_accuracy"][level]))*dist/10))
	return (RingsToAdjust)


with open('club.json', 'r') as f:
	club_data = json.load(f)


def home(request):
	club_type_obj = ClubType.objects.all()
	ball_power_obj = BallPower.objects.all()
	club_level_obj = ClubLevel.objects.all()
	if request.method == 'POST':
		club_id = request.POST['club']
		club_obj = Club.objects.get(id=club_id)

		wind = int(request.POST['wind'])/10
		elevation = int(request.POST['elevation'])
		rings = float(request.POST['rings'])
		rings = int(rings*100)
		ball_power = int(request.POST['ball_power'])
		
		club_used = club_obj.name
		level = int(request.POST['club_level'])

		request.session['club_used']= club_used
		request.session['club_id']= request.POST['club']
		request.session['wind']= request.POST['wind']
		request.session['elevation']= request.POST['elevation']
		request.session['rings']= request.POST['rings']
		request.session['ball_power']= request.POST['ball_power']
		request.session['club_level']= request.POST['club_level']
		

		from_max = (distance_from_max(club_data[club_used], rings, level-1, ball_power))
		from_min = (distance_from_min(club_data[club_used], rings, level-1, ball_power))
		rings_from_max = round((rings_to_adjust(club_data[club_used], level-1, from_max, wind, elevation)), 1)
		rings_from_min =  round((rings_to_adjust(club_data[club_used], level-1, from_min, wind, elevation)),1)
		print (club_used, "\b :", rings_from_max, "|", rings_from_min, "     ", from_max, "|", from_min)
		context = {
			'club_type_obj':club_type_obj,
			'ball_power_obj':ball_power_obj,
			'club_level_obj':club_level_obj,
			'club_used':club_used,
			'rings_from_max':rings_from_max,
			'rings_from_min':rings_from_min,
			'from_max':from_max,
			'from_min':from_min
		}
		return render(request,'Data/home.html',context)
		
	context = {
		'club_type_obj':club_type_obj,
		'ball_power_obj':ball_power_obj,
		'club_level_obj':club_level_obj
	}
	return render(request,'Data/home.html',context)

@csrf_exempt
def getClubs(request):
	club_type_obj = ClubType.objects.get(name=request.POST['typeName'])
	request.session['type_name']= request.POST['typeName']
	club_obj = Club.objects.filter(type=club_type_obj).values()
	club_list = list(club_obj)
	return JsonResponse({'status': 1, 'club_list':club_list})