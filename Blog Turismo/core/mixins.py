from django.contrib.auth.mixins import UserPassesTestMixin

class Super_autor_mixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()

        if hasattr(obj, 'autor'):
            return usuario == obj.autor or usuario.is_superuser or usuario == obj.articulo.autor
    

class Colab_Mixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_colaborador or self.request.user.is_superuser