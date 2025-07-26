import click
import yaml
import logging
from clo3d_generator.config import AppConfig
from clo3d_generator.measurements import MeasurementParser
from clo3d_generator.clo3d import CLO3DClient
from clo3d_generator.storage import CloudStorage
from clo3d_generator.exceptions import CLO3DError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@click.command()
@click.argument('measurements_file', type=click.Path(exists=True))
@click.argument('design_type')
@click.option('--config', '-c', default='config.yaml', help='Configuration file path')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
def main(measurements_file: str, design_type: str, config: str, verbose: bool):
    """Generate clothing images using CLO3D API and store in Google Cloud."""
    
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Load configuration
        with open(config, 'r') as f:
            config_data = yaml.safe_load(f)
        app_config = AppConfig(**config_data)
        
        if design_type not in app_config.designs:
            raise click.BadParameter(f"Design type must be one of: {list(app_config.designs.keys())}")
        
        # Parse measurements
        parser = MeasurementParser()
        measurements = parser.parse(measurements_file)
        
        # Generate image
        clo3d = CLO3DClient(app_config.clo3d_api_key)
        design_id = app_config.designs[design_type]
        logger.info(f"Generating image for design {design_id}")
        image_data = clo3d.generate_image(design_id, measurements)
        
        # Upload to cloud storage
        storage = CloudStorage(app_config.gcs_bucket)
        url = storage.upload_image(image_data, design_id)
        
        click.echo(f"Image generated and uploaded successfully: {url}")
    
    except CLO3DError as e:
        logger.error(str(e))
        raise click.ClickException(str(e))
    except Exception as e:
        logger.exception("Unexpected error occurred")
        raise click.ClickException(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()