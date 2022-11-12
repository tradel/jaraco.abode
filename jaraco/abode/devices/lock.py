"""Abode lock device."""

from ..devices import Device
from ..helpers import constants as CONST


class Lock(Device):
    """Class to represent a door lock."""

    def lock(self):
        """Lock the device."""
        success = self.set_status(CONST.STATUS_LOCKCLOSED_INT)

        if success:
            self._state['status'] = CONST.STATUS_LOCKCLOSED

        return success

    def unlock(self):
        """Unlock the device."""
        success = self.set_status(CONST.STATUS_LOCKOPEN_INT)

        if success:
            self._state['status'] = CONST.STATUS_LOCKOPEN

        return success

    @property
    def is_locked(self):
        """
        Get locked state.

        Err on side of caution, assume if lock isn't closed then it's open.
        """
        return self.status in CONST.STATUS_LOCKCLOSED
