
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods

from .forms import PairingRequestForm
from .models import Pairing
from mentorship_profile.models import Mentor, Mentee

ACCEPT_VALUE = "accept"
REJECT_VALUE = "reject"


@login_required
@require_GET
def pairing_detail_view(request, pairing_id):
    """Return the requested pairing.

    if user.id is one of the mentor or mentee for this pairing AND
    pairing.stats is 'Active':
        display contact info for both.
    """
    pairing_inst = Pairing.objects.filter(id=pairing_id).first()
    if pairing_inst:
        is_user_in_pairing = pairing_inst.is_user_in_pairing(request.user)
        return render(
            request,
            'mentorship_pairing/pairing_detail.html',
            {
                'pairing': pairing_inst,
                'is_user_in_pairing': is_user_in_pairing
            }
        )
    raise Http404("Invalid pairing id: {}".format(pairing_id))


@login_required
@require_http_methods(["GET", "POST"])
def pairing_respond_view(request, pairing_id):
    """Respond to a pairing requrest.

    GET: Return information for the pairing request.
    POST:
        ACCEPT:
            Change pairing status to 'Active'
            Create notification for Requestor.
            Redirect to Pairing Detail Page

        REJECT:
            Delete pairing
            Create notification for Requestor.
            Redirect to 'Thank you.'
    """
    pairing_inst = Pairing.objects.filter(id=pairing_id).first()
    if pairing_inst is None:
        raise Http404

    if request.method == "POST":
        if request.POST['response'] == ACCEPT_VALUE:
            pairing_inst.status = 'active'
            pairing_inst.save()
            # TODO: Send notifications
            return redirect('pairing_accepted', pairing_id=pairing_inst.id)

        if request.POST['response'] == REJECT_VALUE:
            pairing_inst.status = 'rejected'
            pairing_inst.save()
            # TODO: Send notifications
            return redirect('pairing_rejected', pairing_id=pairing_inst.id)

        return HttpResponseBadRequest(
            content=b'<h3>Bad Request (400): invalid form data.'
        )

    elif request.method == "GET":
        return render(
            request,
            'mentorship_pairing/pairing_respond.html',
            {
                'accept_value': ACCEPT_VALUE,
                'reject_value': REJECT_VALUE,
                'pairing_inst': pairing_inst,
            }
        )


@login_required
@require_http_methods(['GET', 'POST'])
def pairing_request_view(request, mentee_id, mentor_id):
    """Request pairing view.

    GET:
        request.user MUST equal pairing_inst.requestee
        Return a form for a pairing request.
    POST:
        Create pairing with form, status='Pending'
        Create notification for requestee
        Send an Email
        Redirect to 'Thank you, a notification has been sent.'
    """
    # TODO: Verifiy that mentee_id belongs to a mentee, mentor_id belongs to
    # a mentor
    mentor = Mentor.objects.filter(id=mentor_id).first()
    mentee = Mentee.objects.filter(id=mentee_id).first()
    if mentor is None or mentee is None:
        raise Http404

    if request.method == 'POST':
        pairing_request_form = PairingRequestForm(
            request.POST,
            prefix='pairing'
        )

        if pairing_request_form.is_valid():
            pairing = pairing_request_form.save(commit=False)
            pairing.requested_by = request.user.profile
            pairing.mentor = mentor
            pairing.mentee = mentee
            pairing.save()
            # TODO: Notification page
            return redirect('private_profile')

    if request.method == 'GET':
        pairing_request_form = PairingRequestForm(prefix='pairing')

    return render(
        request,
        'mentorship_pairing/pairing_request.html',
        {
            'mentor': mentor,
            'mentee': mentee,
            'form': pairing_request_form
        }
    )


@login_required
@require_http_methods(['GET', 'POST'])
def pairing_discontinue_view(request, pairing_id):
    """Discontinue a pairing.

    GET: If user is in pairing, return a form for pairing discontinue.
    POST:
        Delete pairing. ???
        Create notification to other party w/reason.
        Redirect to private profile
    """
    pairing_inst = Pairing.objects.filter(id=pairing_id).first()
    if pairing_inst is None:
        raise Http404

    if not pairing_inst.is_user_in_pairing(request.user):
        raise PermissionDenied

    if request.method == "POST":
        # TODO: Discontinue reason
        discontinue_pairing = request.POST.get('discontinue', False)
        if discontinue_pairing and discontinue_pairing == 'True':
            pairing_inst.status = "discontinued"
            pairing_inst.save()
            return redirect('private_profile')
        return HttpResponseBadRequest(
            content=b'<h3>Bad Request (400): invalid form data.'
        )

    if request.method == "GET":
        return render(
            request,
            'mentorship_pairing/pairing_discontinue.html',
            {"pairing_inst": pairing_inst}
        )


@login_required
@require_GET
def pairing_accepted_view(request, pairing_id):
    """Accepted a pairing.

    GET: Return contact info of other person, link to their profile, link to
    user's profile.
    """
    return render(request, 'mentorship_pairing/pairing_accepted.html')


@login_required
@require_GET
def pairing_rejected_view(request, pairing_id):
    """Rejected a pairing.

    GET: Return notice of rejection, link to user's profile
    """
    pairing_inst = Pairing.objects.filter(pk=pairing_id).first()
    if pairing_inst is None:
        raise Http404
    return render(
        request,
        'mentorship_pairing/pairing_rejected.html',
        {'pairing_inst': pairing_inst}
    )
