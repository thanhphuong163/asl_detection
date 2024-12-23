import hydra
import logging
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base="1.3", config_path="../configs", config_name="config")
def main(cfg: DictConfig):
    logging.info(f"\n{OmegaConf.to_yaml(cfg)}")


if __name__ == "__main__":
    main()
