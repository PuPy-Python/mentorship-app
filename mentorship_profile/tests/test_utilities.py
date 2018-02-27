import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Define a factory for creating user objects."""

    class Meta:
        """Assign a model."""

        model = User

    username = factory.Sequence(lambda n: "Test user {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@example.com".format(x.username.replace(" ", ""))
    )
