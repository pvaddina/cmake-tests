
#ifndef MYMATH_EXPORTS_H
#define MYMATH_EXPORTS_H

#ifdef SHARED_EXPORTS_BUILT_AS_STATIC
#  define MYMATH_EXPORTS
#  define MYMATH_NO_EXPORT
#else
#  ifndef MYMATH_EXPORTS
#    ifdef mymath_EXPORTS
        /* We are building this library */
#      define MYMATH_EXPORTS __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define MYMATH_EXPORTS __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef MYMATH_NO_EXPORT
#    define MYMATH_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef MYMATH_DEPRECATED
#  define MYMATH_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef MYMATH_DEPRECATED_EXPORT
#  define MYMATH_DEPRECATED_EXPORT MYMATH_EXPORTS MYMATH_DEPRECATED
#endif

#ifndef MYMATH_DEPRECATED_NO_EXPORT
#  define MYMATH_DEPRECATED_NO_EXPORT MYMATH_NO_EXPORT MYMATH_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef MYMATH_NO_DEPRECATED
#    define MYMATH_NO_DEPRECATED
#  endif
#endif

#endif /* MYMATH_EXPORTS_H */
