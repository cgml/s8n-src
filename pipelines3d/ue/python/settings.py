class AppContext:
    DATA_DIR = 'C:/s8n/system/s8n-src/_data/render_jobs'
    RENDER_PIPELINE_FRAMES_QUEUE_DIR = f'{DATA_DIR}/render_frames_queue'
    RENDER_PIPELINE_FRAMES_COMPLETED_DIR = f'{DATA_DIR}/render_frames_completed'

    # TODO must be generated automatically from date
    RENDER_ROOT_DIR = "C:/s8n-generated/ue/assembler/20230122-yt1ad"
    RENDER_SEQUENCES_DIR = f'{RENDER_ROOT_DIR}/sequences'
    RENDER_FINAL_DIR = f'{RENDER_ROOT_DIR}/final'

    render_callback = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AppContext, cls).__new__(cls)
        return cls.instance

app_context = AppContext()
