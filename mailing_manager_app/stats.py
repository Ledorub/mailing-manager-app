from django.db.models import Count


def get_mailings_stats(mailings):
    """
    Counts messages for each mailing and groups them by status.
    :param mailings: Mailings to get stats for.
    :type mailings: django.db.models.query.QuerySet
    :return: List of stats.
    :rtype: list
    """
    stats = []
    for mailing in mailings:
        mailing_stats = mailing.messages.values_list('status').annotate(
            Count('status')
        )
        mailing_stats = dict(
            id=mailing.id,
            msg=mailing.msg,
            stats=dict(mailing_stats)
        )
        stats.append(mailing_stats)
    return stats
