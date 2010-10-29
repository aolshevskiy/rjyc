import sbt._

class Plugins(info: ProjectInfo) extends PluginDefinition(info) {
  val java = "net.ps" % "java-project" % "1.0"
}
