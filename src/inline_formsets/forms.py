from django.forms.models import inlineformset_factory, BaseInlineFormSet
from .models import Parent, Child, Address

ChildrenFormset = inlineformset_factory(Parent, Child, extra=1, fields='__all__')
AddressFormset = inlineformset_factory(Child, Address, extra=1, fields='__all__')


class BaseChildrenFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        super(BaseChildrenFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = AddressFormset(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='address-%s-%s' % (
                            form.prefix,
                            AddressFormset.get_default_prefix()),
                        )

    def is_valid(self):
        result = super(BaseChildrenFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):

        result = super(BaseChildrenFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


ChildrenFormset = inlineformset_factory(Parent,
                                        Child,
                                        formset=BaseChildrenFormset,
                                        extra=1,
                                        fields='__all__')
