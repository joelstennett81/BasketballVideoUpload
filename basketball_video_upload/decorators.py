from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.is_administrator:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return _wrapped_view


def player_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.is_player:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return _wrapped_view
