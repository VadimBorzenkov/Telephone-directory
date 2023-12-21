from functools import reduce
from operator import or_

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views import View
from django.db.models import Q
from django.urls import reverse_lazy

from common.views import TitleMixin
from users.forms import UserForm, EditForm, EditSurnameForm, SurnameForm, FirtsnameForm, PatronymicForm, StreetForm, EditFirstnameForm, EditPatronymicForm, EditStreetForm
from users.models import Main, Firstname, Surname, Patronymic, Street


class IndexView(TitleMixin, TemplateView):
    template_name = 'users/index.html'
    tittle = 'Home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Main.objects.all()
        return context


class SearchView(View):
    template_name = 'users/search.html'
    results_template_name = 'users/search_result.html'

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)

        if form.is_valid():
            # Создаем список Q-объектов для фильтрации записей
            q_filters = []

            # Добавляем условие "и" только если поле заполнено
            if form.cleaned_data['surname']:
                q_filters.append(Q(surname__name=form.cleaned_data['surname']))

            if form.cleaned_data['firstname']:
                q_filters.append(
                    Q(firstname__name=form.cleaned_data['firstname']))

            if form.cleaned_data['patronymic']:
                q_filters.append(
                    Q(patronymic__name=form.cleaned_data['patronymic']))

            if form.cleaned_data['street']:
                q_filters.append(Q(street__name=form.cleaned_data['street']))

            # Add additional filters for related fields
            if form.cleaned_data['house']:
                q_filters.append(Q(house=form.cleaned_data['house']))

            if form.cleaned_data['corpus']:
                q_filters.append(Q(corpus=form.cleaned_data['corpus']))

            if form.cleaned_data['apartments']:
                q_filters.append(Q(apartments=form.cleaned_data['apartments']))

            if form.cleaned_data['phone']:
                q_filters.append(Q(phone=form.cleaned_data['phone']))

            # Исключаем результаты, если хотя бы одно условие не выполняется
            search_results = Main.objects.all()

            for q_filter in q_filters:
                search_results = search_results.filter(q_filter)

            # Проверяем, есть ли результаты поиска
            if not search_results.exists():
                return render(request, self.results_template_name, {'no_results': True})

            # Возвращаем результаты поиска в шаблон
            return render(request, self.results_template_name, {'results': search_results})

        # Возвращаем форму с ошибками, если форма не прошла валидацию
        return render(request, self.template_name, {'form': form})


class AddRecordView(View):
    template_name = 'users/add_record.html'
    succsess_url = 'users/index.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            # Проверяем и создаем новые значения в соответствующих таблицах, если они отсутствуют
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            street = form.cleaned_data['street']

            Firstname.objects.get_or_create(name=firstname)
            Surname.objects.get_or_create(name=surname)
            Patronymic.objects.get_or_create(name=patronymic)
            Street.objects.get_or_create(name=street)

            # Создаем запись в основной таблице
            Main.objects.create(
                firstname=Firstname.objects.get(name=firstname),
                surname=Surname.objects.get(name=surname),
                patronymic=Patronymic.objects.get(name=patronymic),
                street=Street.objects.get(name=street),
                house=form.cleaned_data['house'],
                corpus=form.cleaned_data['corpus'],
                apartments=form.cleaned_data['apartments'],
                phone=form.cleaned_data['phone']
            )

            return redirect('index')
        return render(request, self.template_name, {'form': form})


class EditRecordView(UpdateView):
    template_name = 'users/edit_record.html'
    model = Main
    form_class = EditForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Main, pk=self.kwargs['pk'])


def delete_record(request, pk):
    record = Main.objects.get(pk=pk)
    record.delete()
    return redirect('index')


class IndexSurnameView(TitleMixin, TemplateView):
    template_name = 'users/surnames.html'
    tittle = 'Surnames'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Surname.objects.all()
        return context


def delete_record_surname(request, pk):
    record = Surname.objects.get(pk=pk)
    record.delete()
    return redirect('surnames')


class EditRecordSurnameView(UpdateView):
    template_name = 'users/edit_record_surname.html'
    model = Surname
    form_class = EditSurnameForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('surnames')

    def get_object(self, queryset=None):
        return get_object_or_404(Surname, pk=self.kwargs['pk'])


class AddRecordSurnameView(View):
    template_name = 'users/add_record_surname.html'
    succsess_url = 'users/surnames.html'

    def get(self, request):
        form = SurnameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SurnameForm(request.POST)
        if form.is_valid():
            # Проверяем и создаем новые значения в соответствующих таблицах, если они отсутствуют
            surname = form.cleaned_data['name']

            # Surname.objects.get_or_create(name=surname)

            # Создаем запись в таблице фамилий
            Surname.objects.create(name=surname)

            return redirect('surnames')
        return render(request, self.template_name, {'form': form})


class IndexFirstnameView(TitleMixin, TemplateView):
    template_name = 'users/firtnames.html'
    tittle = 'Firstnames'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Firstname.objects.all()
        return context


def delete_record_firstname(request, pk):
    record = Firstname.objects.get(pk=pk)
    record.delete()
    return redirect('firstnames')


class EditRecordFirtnameView(UpdateView):
    template_name = 'users/edit_record_firstname.html'
    model = Firstname
    form_class = EditFirstnameForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('firstnames')

    def get_object(self, queryset=None):
        return get_object_or_404(Firstname, pk=self.kwargs['pk'])


class AddRecordFirstnameView(View):
    template_name = 'users/add_record_firstname.html'
    succsess_url = 'users/firstnames.html'

    def get(self, request):
        form = FirtsnameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FirtsnameForm(request.POST)
        if form.is_valid():
            # Проверяем и создаем новые значения в соответствующих таблицах, если они отсутствуют
            firstname = form.cleaned_data['name']

            # Создаем запись в таблице фамилий
            Firstname.objects.create(name=firstname)

            return redirect('firstnames')
        return render(request, self.template_name, {'form': form})


class IndexPatronymicView(TitleMixin, TemplateView):
    template_name = 'users/patronymics.html'
    tittle = 'Patronymics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Patronymic.objects.all()
        return context


def delete_record_patronymic(request, pk):
    record = Patronymic.objects.get(pk=pk)
    record.delete()
    return redirect('patronymics')


class EditRecordPatronymicView(UpdateView):
    template_name = 'users/edit_record_patronymic.html'
    model = Patronymic
    form_class = EditPatronymicForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('patronymics')

    def get_object(self, queryset=None):
        return get_object_or_404(Patronymic, pk=self.kwargs['pk'])


class AddRecordPatronymicView(View):
    template_name = 'users/add_record_patronymic.html'
    succsess_url = 'users/patronymics.html'

    def get(self, request):
        form = PatronymicForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FirtsnameForm(request.POST)
        if form.is_valid():
            # Проверяем и создаем новые значения в соответствующих таблицах, если они отсутствуют
            patronymic = form.cleaned_data['name']

            # Создаем запись в таблице фамилий
            Patronymic.objects.create(name=patronymic)

            return redirect('patronymics')
        return render(request, self.template_name, {'form': form})


class IndexStreetView(TitleMixin, TemplateView):
    template_name = 'users/streets.html'
    tittle = 'Streets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Street.objects.all()
        return context


def delete_record_street(request, pk):
    record = Street.objects.get(pk=pk)
    record.delete()
    return redirect('streets')


class EditRecordStreetView(UpdateView):
    template_name = 'users/edit_record_street.html'
    model = Street
    form_class = EditStreetForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('streets')

    def get_object(self, queryset=None):
        return get_object_or_404(Street, pk=self.kwargs['pk'])


class AddRecordStreetView(View):
    template_name = 'users/add_record_street.html'
    succsess_url = 'users/streets.html'

    def get(self, request):
        form = StreetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StreetForm(request.POST)
        if form.is_valid():
            # Проверяем и создаем новые значения в соответствующих таблицах, если они отсутствуют
            street = form.cleaned_data['name']

            # Создаем запись в таблице фамилий
            Street.objects.create(name=street)

            return redirect('streets')
        return render(request, self.template_name, {'form': form})
