import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base="1.3", config_path="../configs" , config_name="config")
def main(cfg: DictConfig):
    print("Hello from uv-demo!")
    print("My name is Phuong.")
    print(f"{OmegaConf.to_yaml(cfg)}")


if __name__ == "__main__":
    main()