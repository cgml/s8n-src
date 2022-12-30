class AppContext:
    DATA_DIR = 'C:/s8n/system/src/pipelines/s8n-alpha/ue/python/_data/render_jobs'
    RENDER_PIPELINE_FRAMES_QUEUE_DIR = f'{DATA_DIR}/render_frames_queue'
    RENDER_PIPELINE_FRAMES_COMPLETED_DIR = f'{DATA_DIR}/render_frames_completed'

    RENDER_ROOT_DIR = "C:/s8n/system/src/x-generated/ue/music-video-20221028"
    RENDER_SEQUENCES_DIR = f'{RENDER_ROOT_DIR}/sequences'
    RENDER_FINAL_DIR = f'{RENDER_ROOT_DIR}/final'

    render_callback = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AppContext, cls).__new__(cls)
        return cls.instance

app_context = AppContext()