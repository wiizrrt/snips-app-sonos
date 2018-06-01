from snipssonos.shared.use_case import UseCase
from snipssonos.shared.response_object import ResponseSuccess, ResponseFailure

class PlayTrackUseCase(UseCase):

    def __init__(self, device_discovery_service, music_search_service, music_playback_service):
        self.device_discovery_service = device_discovery_service
        self.music_search_service = music_search_service
        self.music_playback_service = music_playback_service

    def process_request(self, request_object):

        device = self.device_discovery_service.get()

        if request_object.track_name:
            results_track = self.music_search_service.search_track(request_object.track_name)
            if len(results_track):
                first_result = results_track[0]
                self.music_playback_service.play(device, first_result)
            else:
                return ResponseFailure.build_resource_error("An error happened")

        return ResponseSuccess()
