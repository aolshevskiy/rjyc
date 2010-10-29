import sbt._

class Plugins(info: ProjectInfo) extends PluginDefinition(info) {
  val repo = "Plugin Repo" at "http://siasia.github.com/maven2"
  val java = "net.ps" % "java-project" % "1.0"
}
