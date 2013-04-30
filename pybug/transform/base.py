import abc


class Transform(object):
    """
    An abstract representation of any n-dimensional transform.
    Provides a unified interface to apply the transform (:meth:`apply`)
    """
    __metaclass__ = abc.ABCMeta

    def apply(self, x, **kwargs):
        """
        Applies this transform to x. If x is `Transformable`,
        x will be handed this transform object to transform itself. If not,
        x is assumed to be a numpy array. The transformation will be non
        destructive, returning the transformed version. Any **kwargs will be
        passed to the specific transform _apply methods (see these for
        documentation on what are available)
        :param x:
        :param kwargs:
        :return:
        """
        try:
            x._transform(self, **kwargs)
        except AttributeError:
            return self._apply(x, **kwargs)

    @abc.abstractmethod
    def _apply(self, x, **kwargs):
        """
        Applies the transform to the array x, returning the result.
        :param x:
        :raise:
        """
        pass


class Transformable(object):
    """
    Interface for transformable objects. When Transform.apply() is called on
     an object, if the object has the method _transform,
     the method is called, passing in self (the transform object). This
     allows for the object to define how it should transform itself.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _transform(self, transform, **kwargs):
        """
        Apply the transform given to the Transformable object.
        """
        pass
