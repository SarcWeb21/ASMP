from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Mentor, Preference, Profile, Information
from django.contrib import messages


def index(request):
    context = {
        'mentors': Mentor.objects.all()
    }
    return render(request, "land.html", context)


def favourite_add(request, id):
    mentor = get_object_or_404(Mentor, id=id)
    if mentor.favourites.filter(id=request.user.id).exists():
        mentor.favourites.remove(request.user)
        Preference.objects.filter(mentor_id=id, user=request.user).delete()
    else:
        mentor.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

    # def favourite_add(request, id):
    #     mentor = get_object_or_404(Mentor, id=id)
    #     if mentor.favourites.filter(id=request.user.id).exists():
    #         mentor.favourites.remove(request.user)
    #         Preference.objects.filter(mentor_id=id, user=request.user).delete()
    #     else:
    #         mentor.favourites.add(request.user)
    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])


def maxscore(max_mentees):
    if max_mentees == 1:
        return 5.0
    elif max_mentees == 2:
        return 9.0
    elif max_mentees == 3:
        return 12.0
    elif max_mentees == 4:
        return 15.0


def favourite_list(request):
    new = Mentor.objects.all().filter(favourites=request.user)
    ids = new.values_list('pk', flat=True)
    for i in ids:
        mentor_update = Mentor.objects.get(id=i)
        mentor_update.maxscore = maxscore(mentor_update.maxmentees)
        if mentor_update.score > mentor_update.maxscore:
            mentor_update.available = False
            mentor_update.save()

    return render(request, 'wishlist.html', {'new': new})


def returnScore(pref):

    if pref == 1:
        return 2
    elif pref == 2:
        return 1.5
    elif pref == 3:
        return 1
    elif pref == 4:
        return 0.5
    elif pref == 5:
        return 0.25


def update(request):
    new = Mentor.objects.all().filter(favourites=request.user)
    ids = new.values_list('pk', flat=True)
    for i in ids:
        preference = request.POST[str(i) + " preference"]
        mentor = request.POST[str(i)]
        user = request.user
        if Preference.objects.all().filter(user=user, mentor_id=int(mentor)).exists():
            a = Preference.objects.get(user=user, mentor_id=int(mentor))
            a.preference_no = int(preference)
            a.save()
            mentor_update = Mentor.objects.get(id=int(mentor))
            mentor_update.score = mentor_update.score + \
                returnScore(a.preference_no)
            mentor_update.save()
        else:
            preference_user = Preference(preference_no=int(
                preference), mentor_id=int(mentor), user=user)
            preference_user.save()

    return render(request, 'wishlist.html', {'new': new})
    # preference = request.POST["2"]

    # mentor = "2"
    # user = request.user
    # if Preference.objects.all().filter(user=user, mentor_id=int(mentor)).exists():
    #     a = Preference.objects.get(user=user, mentor_id=int(mentor))
    #     a.preference_no = int(preference)
    #     a.save()
    # else:
    #     preference_user = Preference(preference_no=int(
    #         preference), mentor_id=int(mentor), user=user)
    #     preference_user.save()
    # preference = request.POST["3"]
    # mentor = "3"
    # user = request.user
    # if Preference.objects.all().filter(user=user, mentor_id=int(mentor)).exists():
    #     a = Preference.objects.get(user=user, mentor_id=int(mentor))
    #     a.preference_no = int(preference)
    #     a.save()
    # else:
    #     preference_user = Preference(preference_no=int(
    #         preference), mentor_id=int(mentor), user=user)
    #     preference_user.save()

    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
