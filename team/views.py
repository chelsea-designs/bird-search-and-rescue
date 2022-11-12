from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import TeamMemberForm
from .models import TeamMember

# Create your views here.
User = get_user_model()


def team(request):
    '''
    View to display team member page
    '''
    members = TeamMember.objects.all().order_by('name')
    context = {
        'members': members,
        'on_about_page': True
    }
    return render(request, 'team/team.html', context)


@login_required
def addTeamMember(request):
    '''
    View to handle displaying add team member form
    and to handle form processing
    '''
    form = TeamMemberForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.save()
            messages.success(request, 'Team member successfully added!')
            return redirect('team')
        else:
            messages.error(
                request,
                'Failed to add the team member, \
                    please ensure the form is correctly filled in'
                )
    return render(request, 'team/team_member_form.html', context)


@login_required
def editTeamMember(request, slug):
    '''
    View to display prefilled form to edit a team member
    and to handle form processing
    '''
    member = get_object_or_404(TeamMember, slug=slug)
    form = TeamMemberForm(instance=member)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES or None,
                              instance=member)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.save()
            messages.success(request, 'Team member successfully updated!')
            return redirect('team')
        else:
            messages.error(request, 'Failed to update team member, \
                please double check the form.')

    context = {
        'form': form,
        'member': member
    }

    return render(request, 'team/team_member_form.html', context)


@login_required
def deleteTeamMember(request, pk):
    '''
    View to handle the deletion of a team member
    '''
    member = get_object_or_404(TeamMember, pk=pk)
    if request.user.is_authenticated:
        member.delete()
        messages.success(request, 'The member has been deleted.')
        return redirect('team')
    else:
        messages.error(request, 'Only employees can delete team members.')
