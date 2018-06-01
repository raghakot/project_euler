from timeit import default_timer as timer


def timeit(method):
    def helper(*args, **kw):
        start = timer()
        result = method(*args, **kw)
        end = timer()
        print("Completed in {:.2f} ms".format((end - start) * 1000))
        return result
    return helper
