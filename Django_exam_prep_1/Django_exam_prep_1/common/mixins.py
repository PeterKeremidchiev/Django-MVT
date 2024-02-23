class AlbumFormViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["album_name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"

        return form

class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form