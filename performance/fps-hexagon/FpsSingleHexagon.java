package de.oth.programs.examplePrograms;

import de.oth.blocklib.Context;
import de.oth.blocklib.Game;
import de.oth.blocklib.GameState;
import de.oth.blocklib.helper.BlockPos;
import de.oth.blocklib.input.events.InputEvent;
import de.oth.programs.BlockLibProgram;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import org.lwjgl.util.vector.Vector3f;

public class FpsSingleHexagon implements BlockLibProgram {
	private final float intervall = 1;
	private Game game;
	private int framesPerCumulation;
	private List<Integer> fpsList = new ArrayList<>(300);
	private float deltaCumulation;
	private float totalTime;

	public static void main(String[] args) {
		//Configuration.ENABLE_WEATHER = false;
		//Configuration.showWireframe = true;
		FpsSingleHexagon program = new FpsSingleHexagon();
		program.game = new Game(program);
		program.game.start();
	}

	@Override
	public void onGameStart() {
		//game.createFilledWorld();
		game.createEmptyWorld();
		Context.getInstance().getUIManager().getRoot().setVisible(false);
		Context.getInstance().getCamera().setPosition(new Vector3f(22,22,22));
		Context.getInstance().getCamera().setYaw(45);
		Context.getInstance().getCamera().setPitch(-35f);
		Context.getInstance().getGame().getGameStateManager().setGameState(GameState.CAMERA_CONTROL);
		Context.getInstance().getEntityManager().getPlayer().setPosition(new Vector3f(0,100,0));
	}

	@Override
	public void onWorldLoaded() {
		var w = Context.getInstance().getWorldInteraction();
		var v = new BlockPos(0,0,0);
		var dim = 16;
		for (int z = -dim; z < dim; z++) {
			for (int x = -dim; x < dim; x++) {
				for (int y = -dim; y < dim; y++) {
					if(-x-y == z  ){
						v.set(x,y,z);
						w.setBlock(v,"stone");
					}
				}
			}
		}
	}

	@Override
	public void update(float deltaTime) {
		logFps(deltaTime);
	}

	private void logFps(float deltaTime) {
		deltaCumulation += deltaTime;
		totalTime += deltaTime;
		framesPerCumulation++;
		if (deltaCumulation >= intervall) {
			fpsList.add(framesPerCumulation);
			framesPerCumulation = 0;
			deltaCumulation %= intervall;
			System.out.println((int)totalTime);
		}
		if(totalTime>=120){
			try {
				var os = new FileOutputStream("fps-single-hexagon.txt", true);
				for (int j = 0, fpsListSize = fpsList.size(); j < fpsListSize; j++) {
					Integer i = fpsList.get(j);
					os.write((j+"," + i + "\r\n").getBytes(StandardCharsets.UTF_8));
				}
			} catch (IOException e) {
				e.printStackTrace();
			}finally {
				System.exit(0);
			}
		}
	}

	@Override
	public void keyPressed(int key) {
		//if (key == GLFW_KEY_PAGE_UP) {
		//	game.getRenderThread().increaseSwap();
		//}
		//if (key == GLFW_KEY_PAGE_DOWN) {
		//	game.getRenderThread().decreaseSwap();
		//}
	}

	@Override
	public void keyReleased(int key) {
	}

	@Override
	public void process_input(InputEvent inputEvent) {

	}

	public void processInput(InputEvent inputEvent) {
	}
}
