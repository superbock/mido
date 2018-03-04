DEFAULT_TEMPO = 500000  # microseconds per quarter note (i.e. 120 bpm in 4/4)
DEFAULT_TICKS_PER_BEAT = 480  # ticks per quarter note
DEFAULT_TIME_SIGNATURE = (4, 4)


def tick2second(tick, ticks_per_beat=DEFAULT_TICKS_PER_BEAT,
                tempo=DEFAULT_TEMPO):
    """
    Convert MIDI ticks to seconds.

    Parameters
    ----------
    tick : int
        MIDI ticks.
    ticks_per_beat : int, optional
        MIDI file time resolution (ticks/pulses per quarter note, PPQN).
    tempo : int, optional
        MIDI file tempo (microseconds per quarter note).

    Returns
    -------
    seconds : float
        Time in seconds.

    """
    scale = tempo * 1e-6 / ticks_per_beat
    return tick * scale


def second2tick(second, ticks_per_beat=DEFAULT_TICKS_PER_BEAT,
                tempo=DEFAULT_TEMPO):
    """
    Convert seconds to MIDI ticks.

    Parameters
    ----------
    second : float
        Time in seconds.
    ticks_per_beat : int, optional
        MIDI file time resolution (ticks/pulses per quarter note, PPQN).
    tempo : int, optional
        MIDI file tempo (microseconds per quarter note).

    Returns
    -------
    ticks : int
        MIDI ticks.

    Notes
    -----
    The returned `ticks` are of type integer, thus normal rounding applies.

    """
    scale = tempo * 1e-6 / ticks_per_beat
    return int(round(second / scale))


def bpm2tempo(bpm, time_signature=DEFAULT_TIME_SIGNATURE):
    """
    Convert beats per minute to MIDI tempo.

    Parameters
    ----------
    bpm : float
        Beats per minute.
    time_signature : tuple, optional
        Time signature.

    Returns
    -------
    tempo : int
        MIDI tempo (microseconds per quarter note).

    Depending on the chosen `time_signature` a bar contains a different
    number of beats. These beats are multiples/fractions of a quarter note,
    thus the returned tempo depends on the time signature.

    Notes
    -----
    The returned `tempo` is of type integer, thus normal rounding applies.

    """
    return int(round(60 * 1e6 / bpm * time_signature[1] / 4.))


def tempo2bpm(tempo, time_signature=DEFAULT_TIME_SIGNATURE):
    """
    Convert MIDI tempo to beats per minute.

    Parameters
    ----------
    tempo : int
        MIDI tempo (microseconds per quarter note).
    time_signature : tuple, optional
        Time signature.

    Returns
    -------
    bpm : float
        Beats per minute.

    Depending on the chosen `time_signature` a bar contains a different number
    of beats. These beats are multiples/fractions of a quarter note, thus the
    returned `bpm` depend on the time signature.

    """
    return 60 * 1e6 / tempo * time_signature[1] / 4.


def tick2beat(tick, ticks_per_beat=DEFAULT_TICKS_PER_BEAT,
              time_signature=DEFAULT_TIME_SIGNATURE):
    """
    Convert MIDI ticks to beats.

    Parameters
    ----------
    tick : int
        MIDI ticks.
    ticks_per_beat : int, optional
        MIDI file time resolution (ticks/pulses per quarter note, PPQN).
    time_signature : tuple, optional
        Time signature.

    Returns
    -------
    beats : float
        Beats.

    """
    return tick / (4. * ticks_per_beat / time_signature[1])


def beat2tick(beat, ticks_per_beat=DEFAULT_TICKS_PER_BEAT,
              time_signature=DEFAULT_TIME_SIGNATURE):
    """
    Convert beats to ticks.

    Parameters
    ----------
    beat : float
        Beats.
    ticks_per_beat : int, optional
        MIDI file time resolution (ticks/pulses per quarter note, PPQN).
    time_signature : tuple, optional
        Time signature.

    Returns
    -------
    ticks : int
        MIDI ticks.

    Notes
    -----
    The returned `ticks` are of type integer, thus normal rounding applies.

    """
    return int(round(beat * 4. * ticks_per_beat / time_signature[1]))
