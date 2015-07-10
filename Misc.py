def datetime_formater(dt):
    dateStr = "{0}.{1}.{2} {3}:{4}:{5}:{6}".format(dt.day, dt.month, dt.year,
                                                   dt.hour, dt.minute,
                                                   dt.second, dt.microsecond)

    return dateStr
